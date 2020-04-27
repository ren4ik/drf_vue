<template>
    <HomeSlot>
        <mu-row>
            <mu-col span="4">

                <mu-button style="margin-top: 20px" @click="addRoom">Добавить комнату</mu-button>
                <div v-for="room in rooms">
                    <p @click="openDialog(room.id)">{{room.creater.username}}</p>
                    <small>{{room.date}}</small>
                </div>

            </mu-col>
            <slot></slot>
        </mu-row>
    </HomeSlot>
</template>

<script>
    import HomeSlot from '../Home'

    export default {
        name: "Room",
        components: {
            HomeSlot
        },
        data() {
            return {
                rooms: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')}
            });
            this.loadRoom()
        },

        methods: {
            loadRoom() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/room/",
                    type: "GET",
                    success: (response) => {
                        this.rooms = response.data.data;
                    }
                })
            },
            openDialog(id) {
                // this.$emit("openDialog", id) // передает в home id
                this.$router.push({
                    name: 'dialog',
                    params: {id: id}
                })
            },
            addRoom() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/room/",
                    type: "POST",
                    success: (response) => {
                        this.loadRoom()
                    },
                    error: (response) => {
                        alert("Ошибка!")
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>
