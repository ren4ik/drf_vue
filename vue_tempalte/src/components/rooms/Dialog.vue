<template>
    <RoomSlot>
        <mu-col span="8">
            <mu-row>
                <mu-col span="4">
                    <mu-row>
                        <AddUsers :room="id"></AddUsers>
                        <mu-row align-items="center" style="margin-top: 20px">
                            <mu-text-field placeholder="Текст не более 100 символов" multi-line :rows="3"
                                           :max-length="100"
                                           v-model="form.textarea" prop="val"></mu-text-field>
                            <mu-button color="red" @click="sendMes">Отправить</mu-button>
                        </mu-row>
                    </mu-row>
                </mu-col>
                <mu-col span="8">
                    <mu-row v-for="dialog in dialogs"
                            direction="column"
                            justify-content="start"
                            align-items="end">
                        <h2>{{dialog.user.username}}</h2>
                        <p>{{dialog.text}}</p>
                        <span>{{dialog.date}}</span>
                    </mu-row>
                </mu-col>
            </mu-row>
        </mu-col>
    </RoomSlot>
</template>

<script>
    import AddUsers from "./AddUsers";
    import RoomSlot from "./Room";

    export default {
        name: "Dialog",
        components: {
            AddUsers,
            RoomSlot
        },
        props: {
            id: '',
            val: ''
        },
        data() {
            return {
                dialogs: '',
                form: {
                    textarea: ''
                },
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')}
            });
            this.loadDialog()
            setInterval(() => {
                    this.loadDialog()
                }, 5000
            )
        },
        methods: {
            loadDialog() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
                    type: "GET",
                    data: {
                        room: this.$route.params.id
                    },
                    success: (response) => {
                        this.dialogs = response.data.data
                    }
                })
            },
            sendMes() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
                    type: "POST",
                    data: {
                        room: this.$route.params.id, //this.id, прямая передача id
                        text: this.form.textarea
                    },
                    success: (response) => {
                        this.loadDialog()
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            }
        }
    }
</script>

<style scoped>

</style>
