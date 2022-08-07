---
tags:
- EffectType
title: EFFECT_ADJUST_EXTRA_HEAL_GOVERNOR
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_EXTRA_HEAL_GOVERNOR
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="CARDINAL_LAYING_ON_OF_HANDS_HEAL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CARDINAL_LAYING_ON_OF_HANDS_HEAL",
		"MODIFIER_GOVERNOR_ADJUST_HEAL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CARDINAL_LAYING_ON_OF_HANDS_HEAL",
		"Amount",
		100
	);
	
```

