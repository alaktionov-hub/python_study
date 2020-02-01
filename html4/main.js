let user = {
	name: 'Tolik',
	getName: function () {
		return this.name
	}
};

function greeting(method) {
	console.log(method());
}



greeting(user.getName)
