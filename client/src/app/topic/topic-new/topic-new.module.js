"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var common_1 = require("@angular/common");
var topic_new_component_1 = require("./topic-new.component");
var ngx_infinite_scroll_1 = require("ngx-infinite-scroll");
var router_1 = require("@angular/router");
var topic_nav_module_1 = require("../topic-nav/topic-nav.module");
var TopicNewModule = (function () {
    function TopicNewModule() {
    }
    return TopicNewModule;
}());
TopicNewModule = __decorate([
    core_1.NgModule({
        imports: [
            common_1.CommonModule,
            ngx_infinite_scroll_1.InfiniteScrollModule,
            router_1.RouterModule,
            topic_nav_module_1.TopicNavModule
        ],
        declarations: [
            topic_new_component_1.TopicNewComponent
        ],
        exports: [
            topic_new_component_1.TopicNewComponent
        ]
    })
], TopicNewModule);
exports.TopicNewModule = TopicNewModule;
