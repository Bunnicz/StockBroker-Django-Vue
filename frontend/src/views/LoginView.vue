<template>
    <AppLogin @login-user="loginUser" />
</template>

<script>
// import { reactive } from "vue";
import store from "@/store";
import AppLogin from '../components/AppLogin'

export default {
    name: 'HomeView',
    components: {
        AppLogin,
    },
    // setup() {
    //     // const model = reactive({ username: "", password: "" });
    //     function loginUser(model) {
    //         store.dispatch("login", model);
    //     }
    //     return {
    //         // model,
    //         loginUser
    //     }
    // }
    methods: {
        loginUser(user) {
            console.log(user)
            store.dispatch("login", user);
            // const res = JSON.stringify(
            // const res = await axios.post('auth/login/', user)
            //     .then(resp => {
            //         console.log(resp.data)

            //     })
            //     .catch(err => {
            //         console.error(err)
            //     })
            // const data = await res.data.tokens
            // console.log(data)

            // this.auth_token = [...this.auth_token, data]
        },
    }
}
</script>
