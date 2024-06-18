<template>
	<div id="hosts-component">
		<TabTitle title="Hôtes" />

		<HostsTable :hosts-data="hosts" />

		<div>
			
		</div>

		<!-- <ul>
			<li v-for="(host, index) in hosts" :key="index">{{ host[1] }}</li>
		</ul> -->
	</div>
</template>

<script>
// import Header from '@/components/Header.vue'
import DashboardServices from '../services/DashboardServices.js';
import TabTitle from '../components/TabTitle.vue';
import HostsTable from '../components/HostsTable.vue';

export default {
	name: 'Hosts',
	data() {
		return {
			hosts: [],
			interval: null
		}
	},

	methods: {
		getHosts() {
			DashboardServices.getHosts()
			.then(response => {
				console.log(JSON.stringify(response.data));
				this.hosts = response.data;
			})
			.catch(error => {
				console.log("error getHosts");
			});
		}
	},

	mounted() {
		// get from db
		// this.getHosts()

		// hardcoded
		this.hosts = [[1,"super-pc",""],[3,"ultrapc",""],[4,"victimpc","default-hash"],[5,"danger","default-hash"],[6,"megapc","default-hash"]];

		// this.interval = setInterval(() => {
		// 	this.getHosts()
		// }, 3000);
	},

	components: {
		TabTitle,
		HostsTable
	}
}
</script>

<style>
#hosts-component {
	color: white;
}
</style>