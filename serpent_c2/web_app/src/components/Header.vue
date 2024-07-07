<template>
	<div>
		<header>
			<div id="logo-container">
				<img src="@/assets/logo.png" width="60px" height="60px" alt="MyC2 Logo">
				<h1 class="text-xl font-semibold">Serpent C2</h1>
			</div>

			<div class="header--links-container">
				<router-link class="header--links" :to="{ name: 'Home' }">Accueil</router-link>
				<router-link class="header--links" :to="{ name: 'Hosts' }">Hôtes</router-link>
				<a class="header--links" href="#">Déconnexion</a>
			</div>
		</header>
	</div>
</template>

<script>
export default {
	name: 'Header',
}
</script>

<style>
header {
	background-color: #206BB0;
	display: flex;
	justify-items: center;
	justify-content: space-between;
	padding: 1rem 6rem;
	/* padding: 1rem; */
}

.header--links-container {
	display: flex;
	align-items: center;
	justify-items: flex-end;
}

.header--links {
	/* margin-left: 16px; */
	text-decoration: none;
	color: #eee;
	font-size: 20px;
	font-weight: 700;
	transition: all .3s;
	padding: 6px 14px;
	border-radius: 4px;
}

.header--links:hover {
	background-color: #045192;
}

#logo-container {
	display: flex;
	align-items: center;
}

#logo-container img {
	margin-right: 20px;
}


#logo-container h1 {
	color: #eee;
}

</style>