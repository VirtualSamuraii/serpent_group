<template>
	<div class="w-full flex flex-col items-center p-4 h-full">

		<!-- <HostsTable class="border-1 border-gray-900 border-collapse border-gray-900" :hosts-data="hosts" @updateCurrentHostEvent="updateCurrentHost" /> -->
		<HostsTable class="flex-1 w-full" :hosts-data="hosts" @updateCurrentHostEvent="updateCurrentHost" />

		<div class="w-full flex flex-col text-gray-100 border-t-4 pt-4 h-2/3">
			<div class="flex h-28 p-2 border mb-4 bg-blue-500 items-center">
				<div class="mr-4">
					<img v-if="current_host[3] == 'windows'" class="w-16 max-h-16" src="../assets/windows.png" alt="windows">
					<img v-if="current_host[3] == 'linux'" class="w-16 max-h-16" src="../assets/linux.png" alt="linux">
					<img v-if="current_host[3] == 'mac'" class="w-16 max-h-16" src="../assets/mac.png" alt="mac">					
				</div>
				<div class="flex flex-col items-start text-md">
					<span @click="copyToClipboard(current_host[1])" class="p-1 pb-0 rounded transition active:bg-blue-500 cursor-pointer w-fit">{{ current_host[1] }}</span>
					<span @click="copyToClipboard(current_host[4])" class="p-1 pb-0 rounded transition active:bg-blue-500 cursor-pointer w-fit">{{ current_host[4] }}</span>
					<p @click="copyToClipboard(current_host[2])" class="italic p-1 pb-0 rounded transition active:bg-blue-500 cursor-pointer w-fit">{{ current_host[2] }}</p>
				</div>
			</div>
					
			<!-- bottom table -->
			<table>
				<thead>
					<tr>
						<th class="border-r border-b">Commande</th>
						<th class="border-r border-b">Réponse</th>
						<th class="border-r border-b w-48">Date de réponse</th>
						<th class="border-r border-b w-28">Statut</th>
						<th class="border-b w-16"></th>
					</tr>
				</thead>
				<tbody class="">
					<tr v-for="(command, index) in commands" :key="index" class="text-center">
						<td class="border-r border-b text-left">{{ command[1] }}</td>
						<td class="border-r border-b"><a :href="command[6]" target="_blank">{{ command[6] }}</a></td>
						<td class="border-r border-b">{{ command[3] }}</td>
						<td class="border-r border-b">{{ (command[4] == 0) ? "En attente" : "Executée" }}</td>
						<td class="border-b">❌</td>
					</tr>
				</tbody>
			</table>

			<!-- footer -->
			<div class="w-full flex mt-auto">
				<div class="flex w-10/12 mr-6">
					<input type="text" ref="command-input" class="w-full text-gray-800 px-2 py-1 rounded rounded-tr-none rounded-br-none" placeholder="Entrez une commande...">
					<button class="bg-green-600 rounded-tr py-1 rounded-br w-20" @click="addCommand">Ajouter</button>
				</div>
				<span class="text-right items-center truncate" ref="status" :title="this.status">{{ this.status }}</span>
			</div>
		</div>

	</div>
</template>

<script>
// @ is an alias to /src
// import RecapWindows from '@/components/RecapWindows.vue'
import HostsTable from '../components/HostsTable.vue';
import DashboardServices from '../services/DashboardServices';

export default {
	name: 'Home',
	data() {
		return {
			hosts: [],
			interval: null,
			current_host: [],
			status: "",
			commands: []
		}
	},

	methods: {
		/**
		 * GET HOSTS
		 */
		getHosts() {
			DashboardServices.getHosts()
			.then(response => {
				this.hosts = response.data;
			})
			.catch(error => {
				console.log("error getHosts");
			});
		},
		
		/**
		 * GET COMMANDS FOR CURRENT HOST
		 */
		getCommands() {
			DashboardServices.getCommands(this.current_host[0])
			.then(response => {
				this.commands = response.data;
			})
			.catch(error => {
				console.log("error getCommands");
			});
		},

		/**
		 * UPDATE CURRENT HOST
		 */
		updateCurrentHost(host) {
			this.current_host = host;
			this.getCommands();
			this.status = `Chargement de ${host[1]} (${host[4]})`;
		},

		addCommand() {
			if (this.current_host.length === 0) {
				this.status = "<!> Selectionnez un hôte <!>"
				return;
			}
			
			if (this.$refs['command-input'].value.length === 0) {
				this.status = "<!> Entrez une commande <!>"
				return;
			}

			var cmd = this.$refs['command-input'].value;
			var host_id = this.current_host[0];

			DashboardServices.addCommandToHost(host_id, cmd)
			.then(response => {
				this.status = "Une commande à été ajoutée l'hôte " + this.current_host[1];
				
				this.$refs['command-input'].value = "";
				
				// update requests
				this.getCommands();
			})
			.catch(error => {
				console.log("error addCommandToHost");
			});
		},

		copyToClipboard(value) {
			navigator.clipboard.writeText(value);
			this.status = "Copié " + value;
		}
	},

	mounted() {
		// get from db
		this.getHosts()

		this.interval = setInterval(() => {
			this.getHosts()
			this.getCommands()
		}, 5000);


	},
	components: {
		// RecapWindows,
		HostsTable
	}
}
</script>

<style>

#hosts-table tbody tr td {
	/* border: 1px solid #eee; */
	padding: 6px 22px;
}

.host-tr {
	transition: all .1s;
}

.host-tr:hover {
	background-color: #206BB0;
	cursor: pointer;
}

/* ---------------------------- */

.menu--tabs-container {
	display: flex;
	flex-direction: column;
	max-width: 75%;
	margin: 30px auto 0;
}

.menu--tabs-top {
	display: flex;
}

.menu--tabs-top * {
	flex-grow: 1;

}
</style>