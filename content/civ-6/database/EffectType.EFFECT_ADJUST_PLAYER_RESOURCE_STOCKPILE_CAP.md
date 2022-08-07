---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_RESOURCE_STOCKPILE_CAP
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_RESOURCE_STOCKPILE_CAP
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="BASILIKOI_PAIDES_ADJUST_RESOURCE_STOCKPILE_CAP"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"BASILIKOI_PAIDES_ADJUST_RESOURCE_STOCKPILE_CAP",
		"MODIFIER_PLAYER_ADJUST_RESOURCE_STOCKPILE_CAP"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"BASILIKOI_PAIDES_ADJUST_RESOURCE_STOCKPILE_CAP",
		"Amount",
		10
	);
	
```

