---
tags:
- EffectType
title: EFFECT_ADJUST_DUPLICATE_INFLUENCE_TOKEN_WHEN_RIVAL_GOVERNMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DUPLICATE_INFLUENCE_TOKEN_WHEN_RIVAL_GOVERNMENT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="CONTAINMENT_DUPLICATETOKENWHENRIVALGOVERNMENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CONTAINMENT_DUPLICATETOKENWHENRIVALGOVERNMENT",
		"MODIFIER_PLAYER_ADJUST_DUPLICATE_INFLUENCE_TOKEN_WHEN_RIVAL_GOVERNMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CONTAINMENT_DUPLICATETOKENWHENRIVALGOVERNMENT",
		"Amount",
		1
	);
	
```

