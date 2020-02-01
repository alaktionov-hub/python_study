let $field = document.getElementById('field');
let ctx = $field.getContext('2d');

let dir = [10, 0];

let dir = new Point(10, 0)

let body = [
	new Point(30, 10),
	new Point(20, 10),
	new Pontt(10, 10),
];

let cherry = [-10, -10];
let food = [100, 100];


setInterval(function () {
	ctx.clearRect(0, 0, 500, 500);

	if (body[0][0] === cherry[0] && body[0][1] === cherry[1]) {
		cherry = [-10, -10];
		body.unshift(move(body[0], dir));
		body.unshift(move(body[0], dir));
	} else if (body[0][0] === food[0] && body[0][1] === food[1]) {
		food = [Math.ceil(Math.random() * 50) * 10, Math.ceil(Math.random() * 50) * 10];
		body.unshift(move(body[0], dir));
	} else {

		let head = move(body[0], dir);

		if (head[0] < 0) {
			head[0] = 490;
		}

		if (head[0] > 490) {
			head[0] = 0;
		}

		if (head[1] < 0) {
			head[1] = 490;
		}

		if (head[1] > 490) {
			head[1] = 0;
		}

		body.unshift(head);
		body.pop();
	}

	ctx.fillStyle = 'red';
	ctx.fillRect(cherry[0], cherry[1], 10, 10);

	ctx.fillStyle = 'green';
	ctx.fillRect(food[0], food[1], 10, 10);

	ctx.fillStyle = 'black';
	for (let block of body) {
		ctx.fillRect(block[0], block[1], 10, 10);
	}
	ctx.fillText('Accountant Oksana', body[0][0] + 10, body[0][1] - 10)

}, 100);


setInterval(function () {
	cherry = [Math.ceil(Math.random() * 50) * 10, Math.ceil(Math.random() * 50) * 10]
}, 5000);


function canChangeDir(dir1, dir2) {
	console.log(dir1, dir2);
	return dir1[0] + dir2[0] !== 0 || dir1[1] + dir2[1] !== 0;
}


document.addEventListener('keydown', function (event) {
	switch (event.key) {
		case 'ArrowRight':
			if (canChangeDir(dir, [10, 0]))
				dir = [10, 0];
			break;
		case 'ArrowLeft':
			if (canChangeDir(dir, [-10, 0]))
				dir = [-10, 0];
			break;
		case 'ArrowUp':
			if (canChangeDir(dir, [0, -10]))
				dir = [0, -10];
			break;
		case 'ArrowDown':
			if (canChangeDir(dir, [0, 10]))
				dir = [0, 10];
			break;
	}
});
