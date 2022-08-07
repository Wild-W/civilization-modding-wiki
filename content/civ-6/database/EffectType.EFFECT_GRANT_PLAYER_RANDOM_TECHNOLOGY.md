---
tags:
- EffectType
title: EFFECT_GRANT_PLAYER_RANDOM_TECHNOLOGY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_PLAYER_RANDOM_TECHNOLOGY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="OXFORD_UNIVERSITY_FREE_TECHS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"OXFORD_UNIVERSITY_FREE_TECHS",
		"MODIFIER_PLAYER_GRANT_RANDOM_TECHNOLOGY",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"OXFORD_UNIVERSITY_FREE_TECHS",
		"Amount",
		2
	);
	
```

