"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var settings_1 = require("../settings");
var http_1 = require("@angular/http");
var PostService = (function () {
    function PostService(http) {
        this.http = http;
    }
    PostService.prototype.getFeed = function (page, perPage, topicId) {
        if (topicId === void 0) { topicId = null; }
        var params = new http_1.URLSearchParams();
        params.set('offset', (String)(page * perPage));
        params.set('limit', (String)(perPage));
        if (topicId)
            params.set('topic_id', (String)(topicId));
        return this.http.get(settings_1.Settings.API_POSTS_URL + 'feed/', params)
            .toPromise()
            .then(function (res) { return res.json(); });
    };
    PostService.prototype.getNew = function (page, perPage, topicId) {
        if (topicId === void 0) { topicId = null; }
        var params = new http_1.URLSearchParams();
        console.log(page * perPage);
        params.set('offset', (String)(page * perPage));
        params.set('limit', (String)(perPage));
        if (topicId)
            params.set('topic_id', (String)(topicId));
        return this.http.get(settings_1.Settings.API_POSTS_URL + 'new/', params)
            .toPromise()
            .then(function (res) { return res.json(); });
    };
    PostService.prototype.getTrending = function (page, perPage, topicId) {
        if (topicId === void 0) { topicId = null; }
        var params = new http_1.URLSearchParams();
        console.log(page * perPage);
        params.set('offset', (String)(page * perPage));
        params.set('limit', (String)(perPage));
        if (topicId)
            params.set('topic_id', (String)(topicId));
        return this.http.get(settings_1.Settings.API_POSTS_URL + 'trending/', params)
            .toPromise()
            .then(function (res) { return res.json(); });
    };
    PostService.prototype.getTop = function (page, perPage, topicId) {
        if (topicId === void 0) { topicId = null; }
        var params = new http_1.URLSearchParams();
        console.log(page * perPage);
        params.set('offset', (String)(page * perPage));
        params.set('limit', (String)(perPage));
        if (topicId)
            params.set('topic_id', (String)(topicId));
        return this.http.get(settings_1.Settings.API_POSTS_URL + 'top/', params)
            .toPromise()
            .then(function (res) { return res.json(); });
    };
    return PostService;
}());
PostService = __decorate([
    core_1.Injectable()
], PostService);
exports.PostService = PostService;
