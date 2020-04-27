<template>
    <mu-row style="margin-top: 20px">
        <mu-select label="Выбрать пользователя" v-model="options">
            <mu-option v-for="(user,index) in list" :value="index" :label="user.attributes.username"></mu-option>
        </mu-select>
        <mu-button color="greenA700" @click="addUsers">Пригласить</mu-button>
    </mu-row>
</template>

<script>
    export default {
        name: "AddUsers",
        props: {
            room: '',
        },
        data() {
            return {
                options: '',
                list: '',
            }
        },
        created() {
            this.loadUsers()
        },
        methods: {
            //список пользователей
            loadUsers() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/users/",
                    type: "GET",
                    success: (response) => {
                        this.list = response.data
                    }
                })
            },
            addUsers() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/users/",
                    type: "POST",
                    data: {
                        room: this.room,
                        user: parseInt(this.options)
                    },
                    success: (response) => {
                        alert("Пользователь добавлен!")
                    },
                    error: (response) => {
                        alert("Пользователь не добавлен!")
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>
