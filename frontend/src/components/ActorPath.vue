<template>
    <div class="container">
        <h3>Number of Connections: {{data.number}}</h3>
        <form @submit="formSubmit">
            <strong>Name1:</strong>
            <input type="text" class="form-control" v-model="name1">
            <strong>Name2:</strong>
            <input type="text" class="form-control" v-model="name2">

            <button class="btn btn-success">Submit</button>
        </form>
        <div class="container">
            <div v-for="connection in connections" v-bind:key="connection.from_person" class="row">
                    <div class="hover-image-container col-sm-4">
                        <img v-if="people[connection.from_person].profile_path" v-bind:src="'https://image.tmdb.org/t/p/w500/' + people[connection.from_person].profile_path" class="img-fluid hover-image">
                        <img v-else src="default.jpg" class="img-fluid hover-image">
                        <div class="hover-image-middle">
                            <div class="hover-image-text">{{people[connection.from_person].name}}</div>
                        </div>
                    </div>
                    <div class="hover-image-container col-sm-4">
                        <img v-if="movies[connection.movie].poster_path" v-bind:src="'https://image.tmdb.org/t/p/w500/' + movies[connection.movie].poster_path" class="img-fluid">
                        <img v-else src="default.jpg" class="img-fluid">
                    </div>
                    <div class="hover-image-container col-sm-4">
                        <img v-if="people[connection.to_person].profile_path" v-bind:src="'https://image.tmdb.org/t/p/w500/' + people[connection.to_person].profile_path" class="img-fluid hover-image">
                        <img v-else src="default.jpg" class="img-fluid hover-image">
                        <div class="hover-image-middle">
                            <div class="hover-image-text">{{people[connection.to_person].name}}</div>
                        </div>
                    </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "ActorPath",
        data() {
            return {
                data: null,
                people: null,
                movies: null,
                connections: null,
                name1: null,
                name2: null,
            };
        },
        created: function () {
            axios
                .get('http://localhost:5000/Kevin%20Bacon/Fernanda%20Urrejola')
                .then(res => {
                    this.data = res.data;
                    this.people = {};
                    for (let i = 0, length = this.data.people.length; i < length; i++) {
                        this.people[this.data.people[i].id] = this.data.people[i];
                    }

                    this.movies = {};
                    for (let i = 0, length = this.data.movies.length; i < length; i++) {
                        this.movies[parseInt(this.data.movies[i].id)] = this.data.movies[i];
                    }
                    this.connections = [];
                    let j = 0;
                    for (let i = 0, length = this.data.connections.length; i < length; i = i + 2) {
                        this.connections[j] = {
                            'from_person': this.data.connections[i][0],
                            'movie': this.data.connections[i][2],
                            'to_person': this.data.connections[i + 1][0],
                        };
                        j++;
                    }
                })
        },
        methods: {
            formSubmit(e) {
                e.preventDefault();
                // let currentObj = this;
                axios.get('http://localhost:5000/' + this.name1 + '/' + this.name2).then(
                    res => {
                        this.data = res.data;
                        this.people = {};
                        for (let i = 0, length = this.data.people.length; i < length; i++) {
                            this.people[this.data.people[i].id] = this.data.people[i];
                        }

                        this.movies = {};
                        for (let i = 0, length = this.data.movies.length; i < length; i++) {
                            this.movies[parseInt(this.data.movies[i].id)] = this.data.movies[i];
                        }
                        this.connections = [];
                        let j = 0;
                        for (let i = 0, length = this.data.connections.length; i < length; i = i + 2) {
                            this.connections[j] = {
                                'from_person': this.data.connections[i][0],
                                'movie': this.data.connections[i][2],
                                'to_person': this.data.connections[i + 1][0],
                            };
                            j++;
                        }
                    }
                )
            }
        }
    }
</script>

<style scoped>
    h3 {
        margin-bottom: 5%;
    }
    /*.hoverize:hover{*/
        /*cursor:pointer;*/
        /*background-color: #9d9d9d;*/
        /*box-shadow: #888888;*/
    /*}*/
    .img-fluid {
        max-height: 200px;
    }
    .hover-image-container {
        position: relative;
        width: 50%;
        text-align: center;
    }

    .hover-image {
        opacity: 1;
        height: auto;
        transition: .5s ease;
        backface-visibility: hidden;
    }

    .hover-image-middle {
        /*transition: .5s ease;*/
        opacity: 0;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        -ms-transform: translate(-50%, -50%);
        text-align: center;
    }

    .hover-image-container:hover .hover-image {
        opacity: 0.3;
    }

    .hover-image-container:hover .hover-image-middle {
        opacity: 1;
    }

    .hover-image-text {
        background-color: #6e82af;
        color: white;
        font-size: 16px;
        padding: 16px 32px;
    }
</style>
