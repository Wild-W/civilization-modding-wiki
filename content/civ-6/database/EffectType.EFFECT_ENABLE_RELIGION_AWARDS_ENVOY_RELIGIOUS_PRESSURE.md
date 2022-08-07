---
tags:
- EffectType
title: EFFECT_ENABLE_RELIGION_AWARDS_ENVOY_RELIGIOUS_PRESSURE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ENABLE_RELIGION_AWARDS_ENVOY_RELIGIOUS_PRESSURE
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="PAPAL_PRIMACY_PRESSURE_ON_ADOPTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"PAPAL_PRIMACY_PRESSURE_ON_ADOPTION",
		"MODIFIER_PLAYER_RELIGION_ENABLE_AWARDS_ENVOY_RELIGIOUS_PRESSURE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"PAPAL_PRIMACY_PRESSURE_ON_ADOPTION",
		"Amount",
		200
	);
	
```

