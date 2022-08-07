---
tags:
- EffectType
title: EFFECT_ADJUST_RELIGION_ANYONE_CONDEMNS_FAVOR
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_RELIGION_ANYONE_CONDEMNS_FAVOR
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="ANYONE_CONDEMNS_FOR_FAVOR"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ANYONE_CONDEMNS_FOR_FAVOR",
		"MODIFIER_RELIGION_ADJUST_ANYONE_CONDEMNS_FAVOR"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ANYONE_CONDEMNS_FOR_FAVOR",
		"Amount",
		25
	);
	
```

