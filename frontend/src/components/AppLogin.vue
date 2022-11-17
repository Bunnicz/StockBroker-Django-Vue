<template>
    <form @submit="onSubmit" class="add-form">
        <div class="form-control">
            <label>Email</label>
            <input type="email" v-model="email" name="email" placeholder="user@example.com" required/>
        </div>
        <div class="form-control">
            <label>Password</label>
            <input type="password" v-model="password" name="password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" minlength="8" required/>
        </div>
    
        <input type="submit" value="Login" class="btn btn-block" />
    </form>
    <div class="auth__action">
        <p>Haven't signed up yet?</p>
        <router-link to="/register">Register</router-link>
    </div>

</template>

<script>
export default {
    name: 'AppLogin',
    data() {
        return {
            email: '',
            password: '',
        }
    },
    emits: ['login-user'],
    methods: {
        onSubmit(e) {
            e.preventDefault()

            const loginUser = {
                email: this.email,
                password: this.password,
            }
            this.$emit('login-user', loginUser)
            // Form clear
            this.email = ''
            this.password = ''
        }
    }
}
</script>

<style scoped>
.add-form {
    margin-bottom: 40px;
}

.form-control {
    margin: 20px 0;
}

.form-control label {
    display: block;
}

.form-control input {
    width: 100%;
    height: 40px;
    margin: 5px;
    padding: 3px 7px;
    font-size: 17px;
}

.auth__action {
    margin-top: 3rem;
    text-align: center;
}
</style>