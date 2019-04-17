// 封装一个代替getElementById的方法
function byId(id) {
    return typeof(id) === "string"? document.getElementById(id): id;
}

// ------------------------ header 图片轮播 --------------------------
var index = 0;
var timer = null;
var header_imgs = byId("header").getElementsByTagName("img");
var len = pics.length;
var dots = byId("dots").getElementsByTagName("span");
var prev = byId("prev");
var next = byId("next");

function slideImg() {
    var header = byId("header");
    console.log(header);
    // 滑过停止定时器，离开启动定时器
    header.onmouseover = function() {
        if (timer) {
            clearInterval(timer);
        }
    }

    header.onmouseout = function() {
        timer = setInterval(function(){
            index++;
            index %= len;
            changeImg();
        }, 1000);
    }

    header.onmouseout();


    // 点击圆点切换
    for (var i=0; i<len; i++) {
        dots[i].id = i;
        dots[i].onclick = function() {
            index = this.id;

            changeImg();
        }
    }


    // 下一张，上一张图片切换按钮
    prev.onclick = function() {
        index--;
        index %= len;
        if (index<0) {
            index = len-1;
        }
        changeImg();
    }

    next.onclick = function() {
        index++;
        index %= len;
        changeImg();
    }

}

function changeImg() {
    for (var i=0; i<len; i++) {
        pics[i].style.display = "none";
        dots[i].className = "";
    }

    pics[index].style.display = "block";
    dots[index].className = "dot-active";
}

slideImg();