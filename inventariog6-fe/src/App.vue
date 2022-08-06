pág 10 de 12
<template>
	<div
		id="app"
		class="app">
		<div class="header">
			<h1>Inventario G6 Misión TIC</h1>
		</div>
		<div id="content">
			<center>
				<form class="login-form">
					<center>
						<img
							src="./assets/log.png"
							class="image-log" />
					</center>
					<label>Usuario</label>
					<br /><input type="text" /><br />
					<label> Contraseña</label><br />
					<input type="password" /><br />
					<button class="boton-login">LOGIN</button>
					<p class="message">
						Not registered? <a href="#">Create an account</a>
					</p>
				</form>
			</center>
		</div>
	</div>
</template>
<script>
export default {
	name: 'App',
	data: function () {},
	methods: {},
	created: function () {},
};
</script>
<style>
body {
	margin: 0 0 0 0;
	background-image: url('./assets/fondo.jpg');
	font-family: 'Roboto', sans-serif;
}
.header {
	margin: 0;
	padding: 0;
	width: 100%;
	height: 10vh;
	min-height: 100px;
	background-color: #5a989e;
	color: #e5e7e9;
	display: flex;
	justify-content: space-between;
	align-items: center;
}
.header h1 {
	width: 30%;
	text-align: center;
}
form {
	min-width: 250px;
	max-width: 450px;
	text-align: center;
	display: flexbox;
	background-color: rgb(255, 255, 255);
	width: 100%;
	height: 100%;
	border-radius: 5px;
	padding: 50px 60px 10px 40px;
	box-shadow: 0 10px 50px 0 rgb(0, 0, 0.25);
	box-sizing: border-box;
	align-items: center;
	margin-top: 5%;
	line-height: 45px;
	font-family: 'Roboto', sans-serif;
}
.image-log {
	width: 30%;
	height: 30%;
}
.image-log:hover {
	transform: scale(1.2);
	cursor: pointer;
}
input {
	border: none;
	border-bottom: 1px solid rgb(0, 0, 0);
	width: 70%;
}
.boton-login {
	text-decoration: none;
	color: rgb(255, 255, 255);
	padding: 10px 20px 10px 20px;
	left: 50%;
	top: 50%;
	position: static;
	letter-spacing: 8px;
	border-radius: 10px;
	background-color: #5a989e;
	border: 0px;
}

.boton-login:hover {
	opacity: 70%;
	color: rgb(253, 253, 253);
	transform: scale(1.2);
	cursor: pointer;
	background-color: #61a1a7;
}
</style>
