import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EnigmaDashBoardComponent } from './enigma-dash-board.component';

describe('EnigmaDashBoardComponent', () => {
  let component: EnigmaDashBoardComponent;
  let fixture: ComponentFixture<EnigmaDashBoardComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [EnigmaDashBoardComponent]
    });
    fixture = TestBed.createComponent(EnigmaDashBoardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
