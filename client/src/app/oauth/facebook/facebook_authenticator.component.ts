import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Params} from '@angular/router';

@Component({
  template: ''
})
export class FacebookAuthenticatorComponent implements OnInit {
  constructor(private activatedRoute: ActivatedRoute) {}

  ngOnInit(): void {
    console.log('init');

    this.activatedRoute.queryParams.subscribe((params: Params) => {
      let code = params['code'];
      console.log('params:');
      console.log(params);
      console.log(code);
    });
  }
}
