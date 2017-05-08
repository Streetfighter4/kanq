import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {Topic} from '../topic';
import {TopicService} from '../topic.service';

@Component({
  selector: 'app-topic-detail',
  templateUrl: './topic-detail.component.html',
  styleUrls: ['./topic-detail.component.css']
})
export class TopicDetailComponent implements OnInit {
  id: number;
  topic: Topic;

  constructor(private route: ActivatedRoute,
              private topicService: TopicService) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.id = +params['id'];

      this.topicService.getDetail(this.id)
        .then(res => this.topic = res);
    });
  }
}
