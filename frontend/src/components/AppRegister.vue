<template>
    <form @submit="onSubmit" class="add-form">
        <div class="form-control">
            <label>Email</label>
            <input type="email" v-model="email" name="email" placeholder="user@example.com" required />
        </div>
        <div class="form-control">
            <label>Username</label>
            <input type="login" v-model="username" name="username" placeholder="Username" required />
        </div>
        <div class="form-control">
            <label>Password</label>
            <input type="password" v-model="password" name="password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" minlength="8" required />
        </div>
        <div class="form-control">
            <label>Confirm Password</label>
            <input type="password" v-model="confirm_password" name="confirm_password" placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" minlength="8" required />
        </div>

        <input type="submit" value="Register" class="btn btn-block" />
    </form>
    <div class="auth__action">
        <p>Already signed up?</p>
        <router-link to="/login">Login</router-link>
    </div>
</template>

<script>
export default {
    name: 'AppRegister',
    data() {
        return {
            email: '',
            username: '',
            password: '',
            confirm_password: '',
        }
    },
    emits: ['register-user'],
    methods: {
        onSubmit(e) {
            e.preventDefault()

            // simple validation
            if (this.password !== this.confirm_password) {
                alert('Passwords do not match')
                return
            }

            const registerUser = {
                email: this.email,
                username: this.username,
                password: this.password,
                // confirm_password: this.confirm_password,
            }
            this.$emit('register-user', registerUser)
            // Form clear
            this.email = ''
            this.username = ''
            this.password = ''
            this.confirm_password = ''
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