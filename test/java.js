let paras = $('h1')
let btnl = $('#button3')
console.log(btnl)
function question1() {
    for (let i of paras) {
        $('h1').html('DOM is easy')
        alert('вы нажали 3 кнопку')
    }

}
let par = $('h1')
let btn1 = $('#button2')
function quest2() {
    for (let x of par) {
        alert('вы нажали кнопку 2')
    }
} let para = $('h1')
let btn2 = $('#button1')
function qu3() {
    for (let y of para) {
        alert('это вроде кнопка 1')
    }
}
$('#button1').on('click', qu3)
$('#button2').on('click', quest2)
$('#button3').on('click', question1)