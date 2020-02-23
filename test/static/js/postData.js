function ajaxForm() {
    let form=new FormData(document.getElementById("test_form"));
    console.log(form);
    let table=document.getElementById("table");
    rows=table.rows;
    let tableData=[];
    for (let i=0;i<rows.length;i++){
        let rowData=[];
        for(let j=0;j<rows[0].cells.length;j++){
            rowData.push(rows[i].cells[j].innerHTML);
        }
        tableData.push(rowData);
    }
    console.log(tableData);
    let data= {
                "sites": [
                { "name":"菜鸟教程" , "url":"www.runoob.com" },
                { "name":"google" , "url":"www.google.com" },
                { "name":"微博" , "url":"www.weibo.com" }
                ]
            };
    console.log(data);
    let atest=document.getElementById('atest');
    $.ajax(atest.href,{
            type:"post",
            data:form,
            dataType: 'json',
            processData:false,
            contentType:false,
            success:function(data){
                console.log(data);
            },
            error:function(e){
                alert("error");
            }
    });
}