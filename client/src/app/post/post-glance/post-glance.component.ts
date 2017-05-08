import {Component, Input, OnInit} from '@angular/core';
import {PostService} from '../post.service';

@Component({
  selector: 'post-glance',
  templateUrl: './post-glance.component.html',
  styleUrls: ['./post-glance.component.css']
})
export class PostGlanceComponent {
  @Input() post;

  constructor(private postService: PostService) { }

  rate(value: number) {
    this.postService.rate(this.post.id, value);
  }
}
