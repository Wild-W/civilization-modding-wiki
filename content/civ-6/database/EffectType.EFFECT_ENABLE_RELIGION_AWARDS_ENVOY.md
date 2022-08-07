---
tags:
- EffectType
title: EFFECT_ENABLE_RELIGION_AWARDS_ENVOY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ENABLE_RELIGION_AWARDS_ENVOY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Enable `Boolean`

## Samples
```SQL {title="RELIGIOUS_UNITY_ENVOY_ON_ADOPTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"RELIGIOUS_UNITY_ENVOY_ON_ADOPTION",
		"MODIFIER_PLAYER_RELIGION_ENABLE_AWARDS_ENVOY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"RELIGIOUS_UNITY_ENVOY_ON_ADOPTION",
		"Enable",
		1
	);
	
```

