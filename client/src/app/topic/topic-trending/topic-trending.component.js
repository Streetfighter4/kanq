"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var paginated_list_component_1 = require("../../paginated-list/paginated-list.component");
var TopicTrendingComponent = (function (_super) {
    __extends(TopicTrendingComponent, _super);
    function TopicTrendingComponent(route, postService, topicService) {
        var _this = _super.call(this) || this;
        _this.route = route;
        _this.postService = postService;
        _this.topicService = topicService;
        return _this;
    }
    TopicTrendingComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.route.params.subscribe(function (params) {
            _this.id = +params['id'];
            _this.topicService.getDetail(_this.id)
                .then(function (res) { return _this.topic = res; });
        });
        _super.prototype.ngOnInit.call(this);
    };
    TopicTrendingComponent.prototype.loadNextPage = function (currentPage, perPage) {
        var _this = this;
        this.postService.getTrending(currentPage, perPage, this.id)
            .then(function (res) { return _this.addPage(res); });
    };
    return TopicTrendingComponent;
}(paginated_list_component_1.PaginatedListComponent));
TopicTrendingComponent = __decorate([
    core_1.Component({
        selector: 'app-topic-trending',
        templateUrl: './topic-trending.component.html',
        styleUrls: ['./topic-trending.component.css']
    })
], TopicTrendingComponent);
exports.TopicTrendingComponent = TopicTrendingComponent;
