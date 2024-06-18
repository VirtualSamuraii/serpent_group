import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Hosts from '../views/Hosts.vue'

Vue.use(VueRouter)

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home
	},
	{
		path: '/hosts',
		name: 'Hosts',
		component: Hosts
	}
	// {
	// 	path: '/',
	// 	name: 'Home',
	// 	component: Home
	// },
]

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes
})

export default router
