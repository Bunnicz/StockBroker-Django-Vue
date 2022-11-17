<template>
    <div>
        <hr />
        <router-link to="/">Home</router-link>
        <span v-if="!isAuthenticated">
            |
            <router-link to="/login">Login</router-link>
            |
            <router-link to="/register">Register</router-link>
        </span>
        <span v-if="isAuthenticated">
            |
            <router-link to="/dashboard">Dashboard</router-link>
            |
            <a href="#" @click.prevent="onLogout">Logout</a>
        </span>
        <hr />
    </div>
</template>

<script>
import store from "../store";
import { computed } from "vue";

export default {
    name: 'NavbarObj',
    setup() {
        return {
            isAuthenticated: computed(() => store.getters.isAuthenticated),
            onLogout: () => store.dispatch("logout")
        }
    }
}
</script>

<style scoped>

</style>