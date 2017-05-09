import {Component, Input, OnInit} from '@angular/core';
import {Topic} from '../../topic/topic';
import {PostService} from '../post.service';

@Component({
  selector: 'post-create',
  templateUrl: './post-create.component.html',
  styleUrls: ['./post-create.component.css']
})
export class PostCreateComponent {
  @Input() topicId: number;
  selectedFileName: string = null;
  title: string;
  description: string;
  fileBase64: string;
  extension: string;

  constructor(private postService: PostService) { }

  changeListener($event): void {
    this.readFile($event.target);
  }

  readFile(inputValue: any) {
    var file: File = inputValue.files[0];
    var myReader: FileReader = new FileReader();

    myReader.onloadend = (e) => {
      this.fileBase64 = myReader.result.split(',')[1];
      this.extension = myReader.result.split(',')[0].split(';')[0].split('/')[1];
      console.log(this.extension);
    };

    myReader.readAsDataURL(file);
  }

  create() {
    console.log('create post');
    this.postService.create(this.topicId, this.fileBase64, this.extension, this.title, this.description);
  }
}
