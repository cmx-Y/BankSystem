import Vue from 'vue'
import Router from 'vue-router'
import ToDoItem from '@/components/ToDoItem'
import ClientSignin from '@/components/ClientSignin'
import ClientPage from '@/components/ClientPage'
import ClientSignUp from '@/components/ClientSignUp'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ClientSignin',
      component: ClientSignin
    },
    {
      path: '/ttt',
      name: 'ToDoItem',
      component: ToDoItem
    },
    {
      path:'/ClientPage',
      name: 'ClientPage',
      component: ClientPage
    },
    {
      path:'/ClientSignUp',
      name:'ClientSignUp',
      component: ClientSignUp
    }
  ]
})
