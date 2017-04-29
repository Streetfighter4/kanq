import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {PostService} from '../post.service';
import {Post} from '../post';

@Component({
  selector: 'app-post-detail',
  templateUrl: './post-detail.component.html',
  styleUrls: ['./post-detail.component.css']
})
export class PostDetailComponent implements OnInit {
  id: number;
  post: Post;

  constructor(private route: ActivatedRoute,
              private postService: PostService) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.id = +params['id'];

      this.postService.getDetail(this.id)
        .then(res => this.post = res);
    });
  }
}
