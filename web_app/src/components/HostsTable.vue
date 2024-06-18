<template>
	<div>
		<table id="hosts-table" class="w-full text-gray-200">
			<thead>
				<tr>
					<th class="border-r border-b">#</th>
					<th class="border-r border-b ">IP</th>
					<th class="border-r border-b">Hostname</th>
					<th class="border-r border-b">Last Ping</th>
					<th class="border-r border-b">OS</th>
					<th class="border-b">MD5 Hash</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="(host, index) in hostsData" :key="index" class="host-tr" @click="updateHost(host)">
					<td class="border-r border-b">{{ host[0] }}</td>
					<td class="border-r border-b">{{ host[4] }}</td>
					<td class="border-r border-b">{{ host[1] }}</td>
					<td class="border-r border-b"></td>
					<td class="border-r border-b">{{ host[3] }}</td>
					<td class="border-b">{{ host[2] }}</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
export default {
	name: 'HostsTable',
	props: {
		// title: String
		hostsData: Array
	},

	methods: {
		updateHost(host) {
			this.$emit('updateCurrentHostEvent', host);
		}
	}
}
</script>

<style>
#hosts-table tbody tr td {
	padding: 6px 22px;
}

.host-tr {
	transition: all .1s;
}

.host-tr:hover {
	background-color: #206BB0;
	cursor: pointer;
}
</style>