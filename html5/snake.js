let $field = document.getElementById('field');
let ctx = $field.getContext('2d');

let x = 10;
let y = 10;

let head = [10, 10];
let dir = [10, 0];

function move(head, dir) {
	return [head[0] + dir[0], head[1] + dir[1]]
}
//ctx.fillRect(10,10,10,10);
setInterval(() => {
	ctx.clearRect(0, 0, 500, 500);
	head = move(head, dir);
	ctx.fillRect(head[0], head[1], 10, 10);
	//x += 10
}, 500)
