<template>
    <mu-container>
        <mu-row>
            <mu-appbar style="width: 100%;" color="primary">
                Чат на Vue.JS
            </mu-appbar>
            <mu-form :model="form" class="mu-demo-form" label-width="100">
                <mu-form-item label="username" help-text="help text">
                    <mu-text-field v-model="login"></mu-text-field>
                </mu-form-item>
                <mu-form-item label="password" >
                    <mu-text-field type="password" v-model="password"></mu-text-field>
                </mu-form-item>
            </mu-form>
            <mu-button @click="setLogin">Inter</mu-button>
        </mu-row>
    </mu-container>
</template>

<script>

    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: ''
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login/",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password
                    },
                    success: (response) => {
                        alert("Данные верны!")
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: "home"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Пароль и логин не верны!")
                        }
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
