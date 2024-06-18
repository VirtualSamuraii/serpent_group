<template>
	<div id="app" class="flex flex-col h-screen w-screen">
		<Header></Header>
		<main class="h-full w-full max-h-screen">
			<router-view class="h-full" />
		</main>
	</div>
</template>

<script>
import Header from '@/components/Header.vue'

export default {
	name: 'App',
	components: {
		Header
	}
}
</script>

<style>
* {
	box-sizing: border-box;
	margin: 0;
	font-family: Arial, Helvetica, sans-serif;
}

#app {
	background-color: #045192;
	width: 100%;
	height: 100%;
}

main {
	max-height: 100vh;
	/* padding: 2rem 6rem; */
}
</style>
