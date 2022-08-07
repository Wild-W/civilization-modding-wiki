---
tags:
- EffectType
title: EFFECT_ADJUST_INFLUENCE_POINTS_PER_TURN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_INFLUENCE_POINTS_PER_TURN
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="CHARISMATICLEADER_INFLUENCEPOINTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CHARISMATICLEADER_INFLUENCEPOINTS",
		"MODIFIER_PLAYER_ADJUST_INFLUENCE_POINTS_PER_TURN"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CHARISMATICLEADER_INFLUENCEPOINTS",
		"Amount",
		2
	);
	
```

