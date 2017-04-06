import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'errors',
  templateUrl: './errors.component.html'
})
export class ErrorsComponent implements OnInit {
  @Input() errors: any;

  constructor() { }

  ngOnInit() {
  }
}
