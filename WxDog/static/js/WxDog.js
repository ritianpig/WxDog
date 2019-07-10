function reqdata(num) {
    $.getJSON("/book/getdata?num=" + num , {}, function (result) {
        var data = eval(result["data"]);
        var html = "";
        for (var i = 0; i < result["data"].length; i++) {
            html += "<tr class='relative' id='ctr'>";
            html += "<td>" + data[i].ebook_id + "</td>"
            html += "<td>" + data[i].classification + "</td>"
            html += "<td>" + data[i].ebook_title + "</td>"
            html += "<td>" + data[i].introduce + "</td>"
            html += "<td>" + data[i].envelope_url + "</td>"
            html += "<td>" + data[i].ebook_price + "</td>"
            html += "<td>" + data[i].total_chapter + "</td>"
            html += "<td>" + data[i].is_pay + "</td>"
            html += "<td>" + data[i].free_trials + "</td>"
            html += "<td data-value='id' data-button='btn'>"
                + "<input type='button' class='btn btn-blue padding5' onclick='edit(this)' value='更改' />" +
                "<button class='btn btn-danger padding5' onclick='del(this)'>" + "删除" + "</button>" + "</td>"
            html += "</tr>";
        }
        $("#a").html(html);
        var count = result["num"];
        exeData(count)
    })
}
function loadData(count) {

    if (count) {
        //ajax请求后，有了count~重新赋值
        $("#PageCount").val(count);
    } else {
        //页面加载时,初始化一个值
        alert("waa");
        $("#PageCount").val("10");
    }

}
function exeData(count) {
    loadData(count);
    loadpage();
}
function loadpage() {
    var myPageCount = parseInt($("#PageCount").val());
    var myPageSize = parseInt($("#PageSize").val());
    var countindex = Math.ceil(myPageCount/myPageSize);
    $("#countindex").val(countindex);
}


function reload() {
    parent.location.reload("#ctr");
}
function add() {
    $("#myModalLabel").text("增加电子书");
    $("#modalevent").attr("onclick", "adddata()");
    $("#myModal").modal('show');
}

function adddata() {
    var data = {
        "ebook_id": $("#in1").val(),
        "classification": $("#in2").val(),
        "ebook_title": $("#in3").val(),
        "introduce": $("#in4").val(),
        "envelope_url": $("#in5").val(),
        "ebook_price": $("#in6").val(),
        "total_chapter": $("#in7").val(),
        "is_pay": $("#in8").val(),
        "free_trials": $("#in9").val()
    };
    console.log(data);
    $.ajax({
        type: "POST",
        url: "/book/adddata",
        cache: false,
        async: true,
        processData: false,
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify(data),
        dataType: "json",
        success:function (message) {
            alert(JSON.stringify(message.message))
        },
        error:function () {
            alert("提交失败")
        }
    });
    $('#myModal').modal('hide');
    window.location.reload()
    // parent.location.reload("#ctr");
}

function del(obj) {
    var tds = $(obj).parent().parent().find('td');
    var data = {
        "ebook_id": tds.eq(0).text()
    };
    $.ajax({
        type: "POST",
        url: "/book/delete",
        cache: false,
        async: true,
        processData: false,
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify(data),
        success:function () {
            alert("删除成功")
        },
        error:function () {
            alert("未知错误")
        }
    });
    parent.location.reload("#ctr");
}

function edit(obj) {
    var tds = $(obj).parent().parent().find('td');
    $("#in1").val(tds.eq(0).text());
    $("#in2").val(tds.eq(1).text());
    $("#in3").val(tds.eq(2).text());
    $("#in4").val(tds.eq(3).text());
    $("#in5").val(tds.eq(4).text());
    $("#in6").val(tds.eq(5).text());
    $("#in7").val(tds.eq(6).text());
    $("#in8").val(tds.eq(7).text());
    $("#in9").val(tds.eq(8).text());
    $("#myModal").modal({show:true})
}

function update() {
    var data = {
        "ebook_id": $("#in1").val(),
        "classification": $("#in2").val(),
        "ebook_title": $("#in3").val(),
        "introduce": $("#in4").val(),
        "envelope_url": $("#in5").val(),
        "ebook_price": $("#in6").val(),
        "total_chapter": $("#in7").val(),
        "is_pay": $("#in8").val(),
        "free_trials": $("#in9").val()
    };
    $.ajax({
        type: "POST",
        url: "/book/update",
        cache: false,
        async: true,
        processData: false,
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify(data),
        dataType: "json",
        success:function (message) {
            console.log(message);
            alert(JSON.stringify(message.message))
        },
        error:function () {
            alert("提交失败")
        }
    });
    $('#myModal').modal('hide');
    window.location.reload()
    // parent.location.reload("#ctr");
}

function searchPic() {
    var data = {
        "picName": $("#seaPic").val(),
    };
    $.ajax({
        type: "POST",
        url: "/fileMgr/searchPic",
        cache: false,
        async: true,
        processData: false,
        contentType: "application/json:charset=utf-8",
        data: JSON.stringify(data),
        dataType: "json",
        success:function (message) {
            console.log(message.resPicNameList);
            console.log(message.message);
            html = ""
            if(message.message == "1") {
                for (var i = 0; i < message.resPicNameList.length; i++) {
                    picSrc = "http://127.0.0.1:5000/static/pic/" + message.resPicNameList[i]
                    html += "<li>"
                    html += "<a href=" + picSrc + ">"
                    html += "<div class=\"main\">"
                    html += "<img class=\"scrollLoading\" height=\"180px\" width=\"180px\" src=" + picSrc + ">"
                    html += "</div>"
                    html += "<div class=\"checkbox\" style=\"position:absolute;top:0;right:0;z-index:1000\">"
                    html += "<input id=\"box\" type=\"checkbox\" name=\"box\" value=" + message.resPicNameList[i] + ">"
                    html += "</div>"
                    html += "<p class=\"pstyle\">" + message.resPicNameList[i] + "</p>"
                    html += "</a>"
                    html += "</li>";
                }
            }
            else {
                alert("没有相关图片")
            }
            $("#showPic").html(html);
        },
        error:function () {
            alert("提交失败")
        }
    })
}
