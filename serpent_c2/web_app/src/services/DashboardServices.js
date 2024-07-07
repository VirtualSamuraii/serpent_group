import axios from 'axios';

// REPLACE WITH YOUR C2 SERVER IP Address
var c2_ip = "127.0.0.1";

const apiClient = axios.create({
	baseURL: 'http://' + c2_ip + ':5000/api/',
	withCredentials: false,
	headers: {
		'Accept': 'application/json',
		'Content-Type': 'application/json'
	}
});

export default {
	/****************
	*** Dashboard ***
	****************/
	
	getHosts() {
		return apiClient.get('/hosts/list');
	},

	getCommands(host_id) {
		return apiClient.get('/commands/list', {
			params: {
				'host_id' : host_id
			}
		});
	},
	
    addCommandToHost(host_id, cmd) {
		return apiClient.post('/commands/add', [host_id, cmd]);
	},


	logout(token) {
		return apiClient.get('/auth/logout.php?token=' + token);
	}
}