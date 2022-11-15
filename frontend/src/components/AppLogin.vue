<template>
    <form @submit="onSubmit" class="add-form">
        <div class="form-control">
            <label>Login</label>
            <input type="login" v-model="login" name="login" placeholder="Login" required/>
        </div>
        <div class="form-control">
            <label>Password</label>
            <input type="password" v-model="password" name="password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" required/>
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
            login: '',
            password: '',
        }
    },
    methods: {
        onSubmit(e) {
            e.preventDefault()

            // simple validation
            if (!this.login) {
                alert('No username provided')
                return
            }
            if (!this.password) {
                alert('No password provided')
                return
            }

            const loginUser = {
                login: this.login,
                password: this.password,
            }
            this.$emit('loginUser', loginUser)
            // Form clear
            this.login = ''
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