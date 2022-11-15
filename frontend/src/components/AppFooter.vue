<template>
    <footer>
        <p>Copyright &copy; 2022</p>
        <!-- <a href="/about">About</a> -->
        <router-link to="/about">About</router-link>
    </footer>
</template>

<script>
export default {
    name: "AppFooter"
}
</script>

<style scoped>
    a {
        color: #333;

    }

    footer {
        margin-top: 30px;
        text-align: center;
    }
</style>