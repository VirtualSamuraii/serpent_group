<template>
	<div>
		<h1>{{ title }}</h1>
	</div>
</template>

<script>
export default {
	name: 'TabTitle',
	props: {
		title: String
	}
}
</script>

<style>
h1 {
	font-weight: 700;
	text-transform: uppercase;
}
</style>