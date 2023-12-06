var fileSelector = document.getElementById('my-file-selector');
// 侦听对文件选择器的更改
fileSelector.addEventListener('change', function () {
    // 获取所选文件
    var file = fileSelector.files[0];
    // 创建新的文件读取器对象
    var reader = new FileReader();
    // 侦听“load”事件，该事件将在文件完全读取时触发
    reader.addEventListener('load', function () {
    // 获取数据：所选文件的url
    const dataURL = reader.result;
    // 使用数据：url 设置元素的 src 属性<img>
    var img = document.getElementById('my-image');
    img.src = dataURL;
    var imageDataInput = document.getElementById('image_data');
    imageDataInput.value = dataURL;
  });     
    // 读取所选文件
    reader.readAsDataURL(file);
});










// //实现上传表单时页面不刷新
// $("#photo_submit").click(function(){
//   $("#form1").attr("target","rfFrame");
// });
// $("#form1").submit(function(){
//   alert('已提交');
// });

$("#photo_submit").click(function(){
  let formData = new FormData();
  let fileObj = document.getElementById('my-file-selector').files[0];
  if (typeof (fileObj) == "undefined" || fileObj.size <= 0) {
    alert("请选择图片");
    return;
}
  // @Param: <input name="regression_html">
  // @Param: myFile.file[0]为第一个文件（单选）,多个文件（多选）则要循环添加
  formData.append('file',fileObj);
  $.ajax({
    url: "/uplord_face",
    data: formData,
    type: "post",
    dataType: "json",
    cache: false,//上传文件无需缓存
    processData: false,//用于对data参数进行序列化处理 这里必须false
    contentType: false, //必须
    success:function(data){
      alert(data.result);
    },
    error:function(jqXHR){
      // 这里是访问失败时被自动调用的代码
      alert(jqXHR);
    }
})
});










// 监听文件上传控件的变化事件
$("#form-group").change(function() {
// 获取用户上传的图片文件
var file = $("#form-group")[0].files[0];
// 创建一个 FileReader 对象
var reader = new FileReader();
// 监听 FileReader 的 load 事件
reader.addEventListener("load", function() {
    // 将读取到的图片数据设置为图片显示区域的背景图
    $("#image1").css("background-image", "url(" + reader.result + ")");
}, false);
// 调用 FileReader 的 readAsDataURL 方法来读取用户上传的图片
reader.readAsDataURL(file);
});


$(document).ready(function() {
// 为 "下载图片" 按钮添加点击事件处理函数
$("#download-button").click(function() {
// 获取图片的 URL
var imageUrl = $("#image").attr("src");
// 创建一个隐藏的 "a" 元素，并设置其 "href" 和 "download" 属性
var downloadLink = document.createElement("a");
downloadLink.href = imageUrl;
downloadLink.download = "image.jpg";
// 将 "a" 元素添加到文档中
document.body.appendChild(downloadLink);
// 点击 "a" 元素，触发下载
downloadLink.click();
// 删除 "a" 元素
document.body.removeChild(downloadLink);
});
});


$.ajax({
url: '/get-image-url',
success: function(imageUrl) {
// 在 div 容器中插入图片
$('#image-container').append('<img src="' + imageUrl + '" class="img-fluid">');
// 在 div 容器中插入下载按钮
$('#image-container').append('<a href="' + imageUrl + '" download><button class="btn btn-primary">下载图片</button></a>');
}
});














//接收图片
$(document).ready(function() {
$('#form2').submit(function(event) {
event.preventDefault();
var formData = new FormData(this);
$.ajax({
  url: '/merge_face',
  type: 'POST',
  data: formData,
  processData: false,
  contentType: false,
  success: function(data) {
    if (data.id==1){
      $('#image').attr('src', 'data:image/jpeg;base64,' + data.result);
    }
    if (data.id==0){
      alert(data.result);
    }
  },
});
});
});   