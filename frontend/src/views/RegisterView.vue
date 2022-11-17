<template>
    <AppRegister @register-user="registerUser" />
</template>

<script>
import store from "@/store";
import AppRegister from '../components/AppRegister'

export default {
    name: 'RegisterView',
    components: {
        AppRegister,
    },
    methods: {
        registerUser(user) {
            console.log(user)
            store.dispatch("register", user);
            // const res = JSON.stringify(
            // await axios.post('auth/signup/', user)
            // .then(resp => {
            //     console.log(resp.data)

            // })
            // // .catch(err => {
            // //     console.error(err)
            // // })
            // .catch(function (error) {
            //     if (error.response) {
            //         // The request was made and the server responded with a status code
            //         // that falls out of the range of 2xx
            //         console.log(error.response.data);
            //         console.log(error.response.status);
            //         console.log(error.response.headers);
            //     } else if (error.request) {
            //         // The request was made but no response was received
            //         // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
            //         // http.ClientRequest in node.js
            //         console.log(error.request);
            //     } else {
            //         // Something happened in setting up the request that triggered an Error
            //         console.log('Error', error.message);
            //     }
            // })
        },
    }
}
</script>