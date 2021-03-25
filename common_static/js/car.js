layui.define(['layer'],function (exports){
    var layer=layui.layer;
    var car={
        init:function(){
            var urs=document.getElementById('list-cont').getElementsByTagName('ul') ; // 商品列表行列表
            var checkinputs=document.getElementsByClassName('check');               // 所有复选框
            var checkall=document.getElementsByClassName('check-all');              // 全选框
            var countpieces=document.getElementsByClassName('Selected-pieces')[0];  // 总共的件数
            var sumtotal=document.getElementsByClassName('pieces-total')[0];           // 总价格
            var batchdeletion=document.getElementsByClassName('batch-deletion')[0]; // 批量删除按钮
            // 计算选中的物品总价格 所有数量和所有小计的和
            function getTotal(){
                var zgs=0,zjg=0;
                for (var i=0;i<urls.length;i++){
                    // 选中的逐个循环进行计算
                    if (urs[i].getElementsByTagName('input')[0].checked){
                        zgs+=parseInt(urls[i].getElementsByClassName('Quantity-input')[0].value);
                        zjg+=parseFloat(urls[i].getElementsByClassName('sum')[0].innerHTML);
                    }
                }
                countpieces.innerHTML=zgs;
                sumtotal.innerHTML='￥'+zjg.toFixed(2);
            }
            // 计算小计 也就是每一个商品的 数量*价格
            function getSubTotal(ul){
                var unitprice=parseFloat(ul.getElementsByClassName('th-su')[0].innerHTML);  // 价格
                var subSum=parseInt(ul.getElementsByClassName('Quantity-input')[0].value);   // 商品数量
                var subTotal=parseFloat(unitprice*subSum);
                ul.getElementsByClassName('sum')[0].innerHTML=subTotal.toFixed(2);
            }
            // 给所有的复选框增加单击事件，如果全选
            for (var i=0;i<checkinputs.length;i++){
                checkinputs[i].onclick=function(){
                    // 三等号直接不用处理类型转换，如果类型不同直接false,如果这个全选的框选中，那么直接将所有的勾打上
                    if(this.className==='check-all check'){
                        for (var j=0;j<checkinputs.length;j++){
                            checkinputs[j].checked=this.checked;
                        }
                    }
                    if(this.checked == false){
                        for (var k=0;k<checkall.length;k++){
                            checkall[k].checked=false;
                        }
                    }
                    getTotal()
                }
            }
            // 单独删除某一条商品信息
            for (var i=0;i<uls.length;i++){
                uls[i].onclick=function(e){
                    e=e||window.event;
                    var el=e.srcElement;
                    var cls=el.className;
                    var input=this.getElementsByClassName('Quantity-input')[0];
                    var less=this.getElementsByClassName('less')[0];
                    var val=parseInt(input.value);
                    var that=this;
                    switch (cls){
                        case 'add layui-btn':
                            input.value=val+1;
                            getSubTotal(this);
                            break;
                        case 'less layui-btn':
                            if(val>1){
                                input.value=val-1;
                            }
                            getSubTotal(this)
                            break;
                        case 'dele-btn':
                            layer.confirm('你确定要删除吗',{yes:function (index,layero){
                                    layer.close(index);
                                    that.parentNode.removeChild(that);
                                    // 发送ajax请求，删除数据库的购物车信息
                                    console.log(that);
                                    var wareid=that.getElementsByClassName("th th-op")[0].getElementsByTagName("p")[0].innerHTML;
                                    var xhr=new XMLHttpRequest();
                                    var url="/shopper/delete.html?wareId="+wareid;
                                    xhr.open("GET",url);
                                    xhr.send();
                                    xhr.onreadystatechange=function(){
                                        if (xhr.readyState==4 && xhr.status==200){
                                            var text=xhr.responseText;
                                            var json=JSON.parse(text)
                                            if (json.state=='sucess'){
                                                layer.confirm('删除成功')
                                                window.location="/shopper/shopcart.html"
                                            }else{
                                                layer.confirm('删除失败')
                                            }
                                            console.log(json)
                                        }
                                    }
                                }})
                            break;
                    }
                    getTotal()
                }
            }
            // 删除全部商品
            batchdeletion.onclick=function(){
                layer.confirm('您确定要全部删除吗',{yes:function(index,layero){
                    layer.close(index)
                        // 发送ajax请求删除数据库购物车信息
                        var userId=document.getElementById("userId").innerHTML
                        var xhr=new XMLHttpRequest();
                        var url="shopper/delete.html?userId="+userId;
                        xhr.open('GET',url)
                        xhr.send()
                        xhr.onreadystatechange=function(){
                            if (xhr.readyState == 4 && xhr.status == 200){
                                var text=xhr.responseText;
                                var json=JSON.parse(text)
                                if(json.state == "success"){
                                    layer.confirm("删除成功！！！")
                                    window.location="/shopper/shopcart.html"
                                }else{
                                    layer.confirm("删除失败")
                                }
                                console.log(json)
                            }
                        }
                    }})
            }
            checkall[0].checked = true;
            checkall[0].onclick();
        }
    }
    exports('car',car)
});