---
tags:
- EffectType
title: EFFECT_ADJUST_NEUTRALIZE_INDEFINITELY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_NEUTRALIZE_INDEFINITELY
>
> * Class: `Unknown`
> * Parameters:
>	* Neutralize `Unknown`

## Samples
```SQL {title="SAMODERZHAVIYE_GOVERNOR_NEUTRALIZE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SAMODERZHAVIYE_GOVERNOR_NEUTRALIZE",
		"MODIFIER_PLAYER_ADJUST_NEUTRALIZE_INDEFINITELY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SAMODERZHAVIYE_GOVERNOR_NEUTRALIZE",
		"Neutralize",
		1
	);
	
```

