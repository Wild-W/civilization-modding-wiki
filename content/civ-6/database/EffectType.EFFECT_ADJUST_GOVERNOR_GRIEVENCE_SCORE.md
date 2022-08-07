---
tags:
- EffectType
title: EFFECT_ADJUST_GOVERNOR_GRIEVENCE_SCORE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GOVERNOR_GRIEVENCE_SCORE
>
> * Class: `Unknown`
> * Parameters:
>	* Score `Integer`
>	* Turns `Integer`

## Samples

```SQL {title="CAPOU_AGHA_ADJUST_GRIEVANCES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CAPOU_AGHA_ADJUST_GRIEVANCES",
		"MODIFIER_GOVERNOR_ADJUST_GRIEVENCE_SCORE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CAPOU_AGHA_ADJUST_GRIEVANCES",
		"Score",
		1
	),
	(
		"CAPOU_AGHA_ADJUST_GRIEVANCES",
		"Turns",
		1
	);
	
```

