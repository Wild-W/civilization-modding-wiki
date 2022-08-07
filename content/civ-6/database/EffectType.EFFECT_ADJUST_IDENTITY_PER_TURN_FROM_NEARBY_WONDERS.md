---
tags:
- EffectType
title: EFFECT_ADJUST_IDENTITY_PER_TURN_FROM_NEARBY_WONDERS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_IDENTITY_PER_TURN_FROM_NEARBY_WONDERS
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`
>	* ForeignCities `Unknown`

## Samples

```SQL {title="POLICY_MANDALA_STATE_WONDER_IDENTITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"POLICY_MANDALA_STATE_WONDER_IDENTITY",
		"MODIFIER_PLAYER_ADJUST_IDENTITY_PER_TURN_FROM_NEARBY_WONDERS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"POLICY_MANDALA_STATE_WONDER_IDENTITY",
		"Amount",
		2
	),
	(
		"POLICY_MANDALA_STATE_WONDER_IDENTITY",
		"ForeignCities",
		1
	);
	
```

