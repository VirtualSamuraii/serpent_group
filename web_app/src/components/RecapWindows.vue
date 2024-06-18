<template>
	<div class="card" :style="'background-color: #' + bgcolor">
		<div class="card--title-container">
			<h2>{{ title }}</h2>
		</div>
		<div>
			<ul>
				<li>"whoami" sur "kali"</li>
				<li>"whoami" sur "kali"</li>
				<li>"whoami" sur "kali"</li>
			</ul>
		</div>
	</div>
</template>

<script>
export default {
	name: 'RecapWindows',
	props: [
		'title',
		'bgcolor'
	]
}
</script>

<style>
.card {
	height: 150px;
	padding: 15px 20px;
	display: flex;
	flex-direction: column;
}

.card--title-container {

}

.card--title-container h2 {
	color: #eee;
}

</style>